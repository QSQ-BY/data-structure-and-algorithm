

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//直接使用数组实现栈而不再用链表或者顺序表封装
typedef struct stack{
    int* data;
    int top;
    int size;
    int count;
}stack;

stack* create_stack(int n){
    if(n <= 0) return nullptr;

    stack* s = (stack*)malloc(sizeof(stack));
    if(s == nullptr) return nullptr;

    s->data = (int*)malloc(sizeof(int) * n);
    if(s->data == nullptr){
        free(s);
        return nullptr;
    }

    s->size = n;
    s->count = 0;
    s->top = -1;
    return s;
}

int empty(stack* s){
    if(s->count == 0) return 1;
    else return 0;
}

//查看栈顶元素
int top(stack* s){
    if(empty(s)) return -1;
    return s->data[s->top];
}

int push(stack* s,int val){
    if(s->count == s->size) return 0;//栈已经满了
    else{
        s->top++;
        s->data[s->top] = val;
        s->count ++;
        return 1;
    }
}

int pop(stack* s){
    if(empty(s)) return 0;
    s->top--;
    s->count--;
    return 1;
}
void clear_stack(stack* s){
    if(s==nullptr) return;
    free(s->data);
    free(s);
    return;
}

void test01(){
    stack* s = create_stack(3);
    int case_id = 1;
    int pass_count = 0;
    int total_count = 0;

    printf("+------+----------------------+----------+----------+----------+\n");
    printf("| Case | Operation            | Expected | Actual   | Result   |\n");
    printf("+------+----------------------+----------+----------+----------+\n");

    int actual = (s != nullptr);
    int pass = (actual == 1);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8d | %-8d | %-8s |\n", case_id++, "create_stack(3)", 1, actual, pass ? "PASS" : "FAIL");

    actual = empty(s);
    pass = (actual == 1);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8d | %-8d | %-8s |\n", case_id++, "empty init", 1, actual, pass ? "PASS" : "FAIL");

    actual = push(s, 10);
    pass = (actual == 1 && top(s) == 10 && s->count == 1);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "push 10", "1,10,1", pass ? "1,10,1" : "ERROR", pass ? "PASS" : "FAIL");

    actual = push(s, 20);
    pass = (actual == 1 && top(s) == 20 && s->count == 2);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "push 20", "1,20,2", pass ? "1,20,2" : "ERROR", pass ? "PASS" : "FAIL");

    actual = push(s, 30);
    pass = (actual == 1 && top(s) == 30 && s->count == 3);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "push 30", "1,30,3", pass ? "1,30,3" : "ERROR", pass ? "PASS" : "FAIL");

    actual = push(s, 40);
    pass = (actual == 0 && top(s) == 30 && s->count == 3);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "push full", "0,30,3", pass ? "0,30,3" : "ERROR", pass ? "PASS" : "FAIL");

    actual = pop(s);
    pass = (actual == 1 && top(s) == 20 && s->count == 2);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "pop once", "1,20,2", pass ? "1,20,2" : "ERROR", pass ? "PASS" : "FAIL");

    pop(s);
    actual = pop(s);
    pass = (actual == 1 && empty(s) == 1 && top(s) == -1 && s->count == 0);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "pop to empty", "1,-1,0", pass ? "1,-1,0" : "ERROR", pass ? "PASS" : "FAIL");

    actual = pop(s);
    pass = (actual == 0 && empty(s) == 1 && s->count == 0);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8s | %-8s | %-8s |\n", case_id++, "pop empty", "0,1,0", pass ? "0,1,0" : "ERROR", pass ? "PASS" : "FAIL");

    stack* bad = create_stack(0);
    actual = (bad == nullptr);
    pass = (actual == 1);
    pass_count += pass;
    total_count++;
    printf("| %-4d | %-20s | %-8d | %-8d | %-8s |\n", case_id++, "create_stack(0)", 1, actual, pass ? "PASS" : "FAIL");

    printf("+------+----------------------+----------+----------+----------+\n");
    printf("Passed: %d / %d\n", pass_count, total_count);

    clear_stack(s);
    clear_stack(bad);
}
int main(void){
    test01();
    system("pause");
    return 0;
}