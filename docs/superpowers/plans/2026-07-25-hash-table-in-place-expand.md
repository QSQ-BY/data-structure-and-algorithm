# Hash Table In-Place Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `expand()` replace the bucket array in place while preserving the `hash_table` object address and releasing the old bucket array.

**Architecture:** Allocate and initialize a doubled bucket array, detach every existing node from the old buckets, and relink it into the new buckets using the new modulus. After migration succeeds, free only the old sentinel array and update `h->data` and `h->size`; `h->cnt`, node addresses, and string allocations remain unchanged.

**Tech Stack:** C++17, MinGW g++, C standard allocation functions

## Global Constraints

- Preserve the existing GBK/CP936 encoding of the source file.
- Keep generated tests and executables under `.build`.
- Modify only expansion-related production logic.
- Do not commit the user's untracked source file unless explicitly requested.

---

### Task 1: Implement and verify in-place expansion

**Files:**
- Modify: `source/lookup_algorithm/base_algorithm/3hash_table&bloom_filter.cpp:25-107`
- Create: `.build/hash_expand_inplace_test.cpp`

**Interfaces:**
- Consumes: `node`, `hash_table`, `hash_func(const char*)`, and the existing insertion/find/cleanup functions.
- Produces: `bool expand(hash_table* h)`; `insert(hash_table* h, const char* s)` returns `false` when expansion fails.

- [ ] **Step 1: Write the failing test**

Create a driver that includes the real source file, inserts 17 one-character keys, and checks:

```cpp
#define main hash_table_original_main
#include "../source/lookup_algorithm/base_algorithm/3hash_table&bloom_filter.cpp"
#undef main

bool check_case(const char* name, bool condition) {
    printf("| %-30s | %-4s |\n", name, condition ? "PASS" : "FAIL");
    return condition;
}

int main() {
    bool passed = true;
    hash_table* h = get_new_hash_table(4);
    hash_table* original_object = h;
    node* initial_data = h->data;
    const char* keys[] = {
        "a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "o", "p", "q"
    };

    for (int i = 0; i < 8; i++) passed = insert(h, keys[i]) && passed;
    int first_count = h->cnt;
    passed = insert(h, keys[8]) && passed;

    printf("+--------------------------------+------+\n");
    printf("| Check                          | Result |\n");
    printf("+--------------------------------+------+\n");
    passed = check_case("object address after first expand", h == original_object) && passed;
    passed = check_case("bucket address after first expand", h->data != initial_data) && passed;
    passed = check_case("size after first expand", h->size == 8) && passed;
    passed = check_case("count after first expand", h->cnt == first_count + 1) && passed;

    node* first_expanded_data = h->data;
    for (int i = 9; i < 17; i++) passed = insert(h, keys[i]) && passed;

    passed = check_case("object address after second expand", h == original_object) && passed;
    passed = check_case("bucket address after second expand", h->data != first_expanded_data) && passed;
    passed = check_case("size after second expand", h->size == 16) && passed;
    passed = check_case("count after second expand", h->cnt == 17) && passed;

    bool all_found = true;
    for (int i = 0; i < 17; i++) all_found = find(h, keys[i]) && all_found;
    passed = check_case("all keys remain findable", all_found) && passed;
    printf("+--------------------------------+------+\n");

    clear_hash_table(h);
    return passed ? 0 : 1;
}
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```powershell
g++ -std=c++17 -Wall -Wextra -Wpedantic -g `
  -o ".build\hash_expand_inplace_test.exe" `
  ".build\hash_expand_inplace_test.cpp"
```

Expected: compilation fails because the current `expand()` calls `insert()` before its declaration and does not implement in-place migration.

- [ ] **Step 3: Implement the minimal production change**

Add `<limits.h>`, replace `expand()`, and update the expansion branch in `insert()`:

```cpp
bool expand(hash_table* h) {
    if (h == nullptr || h->data == nullptr ||
        h->size <= 0 || h->size > INT_MAX / 2) {
        return false;
    }

    int old_size = h->size;
    int new_size = old_size * 2;
    node* old_data = h->data;
    node* new_data = (node*)malloc(sizeof(node) * new_size);
    if (new_data == nullptr) return false;

    for (int i = 0; i < new_size; i++) {
        new_data[i].s = nullptr;
        new_data[i].next = nullptr;
    }

    for (int i = 0; i < old_size; i++) {
        node* p = old_data[i].next;
        while (p != nullptr) {
            node* next = p->next;
            int index = hash_func(p->s) % new_size;
            p->next = new_data[index].next;
            new_data[index].next = p;
            p = next;
        }
    }

    free(old_data);
    h->data = new_data;
    h->size = new_size;
    return true;
}
```

```cpp
if (h->size > 0 && h->cnt / h->size >= 2) {
    if (expand(h) == false) return false;
}
```

- [ ] **Step 4: Run the expansion test**

Run the command from Step 2, then:

```powershell
& ".\.build\hash_expand_inplace_test.exe"
```

Expected: compilation exits with `0`; all nine table rows report `PASS`; test exits with `0`.

- [ ] **Step 5: Compile the original interactive program**

Run:

```powershell
g++ -std=c++17 -Wall -Wextra -Wpedantic -g `
  -o ".build\hash_table_final.exe" `
  "source\lookup_algorithm\base_algorithm\3hash_table&bloom_filter.cpp"
```

Expected: compilation exits with `0` and produces no compiler diagnostics.

- [ ] **Step 6: Verify scope and encoding**

Confirm the source still decodes as CP936, its Chinese comments are readable, and Git shows no unrelated new changes beyond the user's pre-existing work and this requested source edit.
