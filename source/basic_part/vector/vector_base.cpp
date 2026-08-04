//顺序表的基础结构定义与结构操作(C语言)
#include <stdio.h>
#include <stdlib.h>
typedef struct Vector
{
    int *data; // 数组数据
    int size;  // 顺序表大小
    int count; // 顺序表存储的元素个数
} vector;

// 创建操作
vector *create_vector(int size) // 使用指针作为函数返回值，因为函数内部分配的内存需要在函数外部使用，所以必须使用指针来返回分配的内存地址
{
    vector *v = (vector *)malloc(sizeof(vector));
    if (v == nullptr)
    {
        printf("顺序表初始化失败，无法分配顺序表结构体内存");
        return nullptr;
    }
    v->data = (int *)malloc(sizeof(int) * size);
    if (v->data == nullptr)
    {
        printf("顺序表初始化失败，无法分配顺序表数据内存");
        free(v);
        return nullptr;
    }

    printf("顺序表创建成功，大小为%d\n", size);
    v->size = size;
    v->count = 0;
    
    return v;
}

//扩容操作
int expand(vector* v){
    if (v == nullptr) return 0;
    // 二倍扩容法则，至少扩到 1
    int new_size = (v->size > 0) ? (v->size * 2) : 1;
    int *p; // 如果realloc函数返回了空指针，则原来的v->data指针会丢失
    p = (int*)realloc(v->data, sizeof(int) * new_size);
    if (p == nullptr){
        printf("扩容失败\n");
        return 0;
    }
    v->data = p;
    v->size = new_size;
    printf("扩容成功，扩容后的顺序表大小为%d\n", v->size);
    return 1;
}

// 打印操作
int print(vector *v)
{
    if (v == nullptr)
    {
        printf("顺序表为空，无法打印\n");
        return 0;
    }
    printf("当前顺序表: size=%d, count=%d, data=[", v->size, v->count);
    for (int i = 0; i < v->count; i++)
    {
        if (i > 0) printf(", ");
        printf("%d", v->data[i]);
    }
    printf("]\n");
    return 1;
}

// 初始化操作
vector *init_vector(vector *v, int count, int num)
{
    if (v == nullptr || v->data == nullptr || count < 0 || count > v->size)
    {
        printf("顺序表初始化失败，参数无效");
        return v;
    }
    v->count = count;
    for (int i = 0; i < v->count; i++)
    {
        v->data[i] = num;
    }
    printf("成功初始化顺序表\n");
    print(v);
    return v;
}

// 插入操作
int insert(vector *v, int pos, int num)
{
    if (v == nullptr)
    {
        printf("插入无效，顺序表为空\n");
        return 0;
    }
    if (pos < 0 || pos > v->count)
    {
        printf("插入无效，位置无效\n");
        return 0;
    }
    else if ((v->count + 1 > v->size) and (expand(v) == 0) )
    {
        printf("插入无效,容器空间过小无法容纳,且扩容失败\n");
        return 0; 
    }
    else
    {
        for (int i = v->count - 1; i >= pos; i--)
        {
            v->data[i + 1] = v->data[i];
        }
        v->data[pos] = num;
        v->count++;
        printf("成功在%d位置插入%d\n",pos,num);
        return 1;
    }
}

//删除操作（位置删除）
int erase_position(vector* v,int pos){
    if (v == nullptr){
        printf("删除失败，顺序表为空\n");
        return 0;
    }else if (pos < 0 || pos > v->count - 1){
        printf("删除失败，位置无效\n");
        return 0;
    }else{
        int removed = v->data[pos];
        for (int i = pos; i < (v->count) - 1; i++){ // 操作到倒数第二个元素即可
            v->data[i] = v->data[i + 1];
        }
        v->count--;
        printf("成功在%d位置删除%d\n", pos, removed);
        return 1;
    }
}

//删除操作（元素删除）
int erase_number(vector* v,int num){
    if (v == nullptr){
        printf("删除失败，顺序表为空\n");
        return 0;
    }else{
        int removed_count = 0;
        for (int i = 0; i < v->count; i++){
            if (v->data[i] == num){
                erase_position(v, i);
                removed_count++;
                i--; // 删除位置元素的操作会使数组元素整体左移，此时i也应该左移
            }
        }
        if (removed_count == 0){
            printf("未找到需要删除的元素%d\n", num);
        }else{
            printf("共删除%d个元素%d\n", removed_count, num);
        }
        return 1;
    }
}

//更改操作（位置更改）
int change_position(vector* v,int pos,int num){
    if (v == nullptr){
        printf("更改失败，顺序表为空\n");
        return 0;
    }else if (pos < 0 || pos > v->count - 1){
        printf("更改失败，位置无效\n");
        return 0;
    }else{
        int temp = v->data[pos];
        v->data[pos] = num;
        printf("成功在%d位置将%d更改为%d\n", pos, temp, num);
        return 1;
    }
}

//更改操作（数字更改）
int change_number(vector* v,int changed_num,int new_num){
    if (v == nullptr){
        printf("更改失败，顺序表为空\n");
        return 0;
    }else{
        int changed_count = 0;
        for (int i = 0; i < v->count; i++){
            if (v->data[i] == changed_num){
                v->data[i] = new_num;
                changed_count++;
            }
        }
        if (changed_count == 0){
            printf("未找到需要更改的元素%d\n", changed_num);
        }else{
            printf("共更改%d个元素%d为%d\n", changed_count, changed_num, new_num);
        }
        return 1;
    }
}

//销毁操作
void destroy_vector(vector* v){
    if (v == nullptr) return;
    if (v->data != nullptr){
        free(v->data);
        v->data = nullptr;
    }
    v->size = 0;
    v->count = 0;
    free(v);
}


// 操作测试代码
void test01()
{
    int size;
    printf("\n==== 顺序表的初始化测试 ====\n");
    printf("请输入顺序表的大小: ");
    scanf("%d", &size);
    vector *v = create_vector(size);
    print(v);
    printf("\n==== 初始化为 5 个 10 ====\n");
    init_vector(v, 5, 10);
    print(v);
    printf("\n==== 插入: pos=2, num=3 ====\n");
    insert(v, 2, 3);
    print(v);
    printf("\n==== 删除位置: pos=0 ====\n");
    erase_position(v,0);
    print(v);
    printf("\n==== 删除元素: num=3 ====\n");
    erase_number(v,3);
    print(v);
    printf("\n==== 位置更改: pos=3, num=7 ====\n");
    change_position(v,3,7);
    print(v);
    printf("\n==== 元素更改: 10 -> 6 ====\n");
    change_number(v,10,6);
    print(v);

    destroy_vector(v);
    return;
}

int main(void)
{
    test01();
    system("pause");
    return 0;
}