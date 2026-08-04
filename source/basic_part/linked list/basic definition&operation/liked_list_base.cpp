#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//结构定义
typedef struct node{
    int val;
    struct node* next;
}node;

typedef struct both_way_node{
    int val;
    struct both_way_node* pre;
    struct both_way_node* next;
}both_way_node;

//创建链表操作
node* create_node(int val){
    node* p=(node*)malloc(sizeof(node));
    p->val = val;
    p->next = nullptr;
    return p;
}

//创建双向链表操作
both_way_node* create_both_way_node(int val){
    both_way_node* p=(both_way_node*)malloc(sizeof(both_way_node));
    p->val = val;
    p->pre = nullptr;
    p->next = nullptr;
    return p;
}

//删除操作(节点)
node* erase(node* head,int pos){
    if(head == nullptr){
        return head;
    }
    if(pos <= 0){
        node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    node* p = head;
    for(int i=1;i<pos;i++){
        if(p == nullptr){
            return head;
        }
        p = p->next;
    }
    if(p == nullptr || p->next == nullptr){
        return head;
    }
    node* temp = p->next;
    p->next = temp->next;
    free(temp);
    return head;
}

//插入操作1（头节点单独讨论）
node* insert1(node* head,int pos,int val){
    if(pos == 0){
        node* new_head = create_node(val);
        new_head->next = head;
        return new_head;
    }else{
        node* p =head;
        for(int i =1;i<pos;i++){
            if(p == nullptr){
                return head;
            }
            p=p->next;
        }
        if(p == nullptr){
            return head;
        }
        //p指针指向了待插入节点的前一位
        node* new_node = create_node(val);
        new_node->next = p->next;
        p->next = new_node;
        return head;
    }
}

//插入操作2(虚拟头节点)
node* insert2(node* head,int pos,int val){
    node* dummy_head = create_node(0);
    dummy_head->next = head;
    node* p = dummy_head;
    for(int i = 0;i<pos;i++){
        if(p == nullptr){
            break;
        }
        p = p->next;
    }
    if(p == nullptr){
        node* new_head = dummy_head->next;
        free(dummy_head);
        return new_head;
    }
    node* new_node = create_node(val);
    new_node->next = p->next;
    p->next = new_node;
    node* new_head = dummy_head->next;
    free(dummy_head);
    return new_head;
}

//打印操作
void print_linklist(node* head){
    int len = 0;
    node* p = head;
    while(p){
        if(p!=nullptr) len++;
        p=p->next;
    }
    for(int i = 0;i<len;i++){
        printf("%3d",i);
        printf("  ");
    }
    printf("\n");
    for(p=head;p;p=p->next){
        printf("%3d",p->val);
        printf("->");
    }
    printf("\n\n");
    return;
}

//查找操作
int find(node* head,int target){
    int found = 0;
    for(node* p=head;p!=nullptr;p=p->next){
        if(p->val == target){
            found = 1;
            break;
        }
    }
    if(!found){
        return 0;
    }

    print_linklist(head);
    for(node* p=head;p!=nullptr;p=p->next){
        if(p->val == target){
            printf("  ^  ");
        }else{
            printf("     ");
        }
    }
    printf("\n");
    for(node* p=head;p!=nullptr;p=p->next){
        if(p->val == target){
            printf("  |  ");
        }else{
            printf("     ");
        }
    }
    printf("\n");
    return 1; 
}
//销毁操作
void clear(node* head){
    node* p = head;
    while(p){
        node* temp = p->next;
        free(p);
        p = temp;
    }
    return;
}

void clear_both_way(both_way_node* head){
    both_way_node* p = head;
    while(p){
        both_way_node* temp = p->next;
        free(p);
        p = temp;
    }
}

//基础构建与插入测试
void test01(){
    srand(time(0));
    node* head = nullptr;
    for(int i=0;i<10;i++){
        int val = rand()%10;
        int pos = rand()%(i+1);
        printf("insert %d at %d to linklist\n",val,pos);
        head = insert1(head,pos,val);
        print_linklist(head);
    }

    find(head,5);
    clear(head);
}

//查找操作测试
void test02(){
    node* head=nullptr;
    for(int i=0;i<5;i++){
        int val;
        scanf("%d",&val);
        head = insert1(head,i,val);
    }
    find(head,55);
}

//循环链表
void test03(){
    srand(time(0));
    node* head = nullptr;
    for(int i=0;i<10;i++){
        int val = rand()%100;
        int pos = rand()%(i+1);
        head = insert2(head,pos,val);
    }
    print_linklist(head);
    if(head == nullptr){
        return;
    }
    node* tail = head;
    while(tail->next != nullptr){
        tail = tail->next;
    }
    tail->next = head;
    int count = 0;
    for(node* p = head;count <= 15;p = p->next, count++){
        printf("%3d",p->val);
        printf("->");
    }
    printf("...\n");
}

//双向链表
void test04(){
    srand(time(0));
    both_way_node* head = nullptr;
    both_way_node* tail = nullptr;
    for(int i=0;i<8;i++){
        int val = rand()%100;
        both_way_node* new_node = create_both_way_node(val);
        if(head == nullptr){
            head = new_node;
            tail = new_node;
        }else{
            tail->next = new_node;
            new_node->pre = tail;
            tail = new_node;
        }
    }

    printf("forward:  ");
    for(both_way_node* p=head;p;p=p->next){
        printf("%3d",p->val);
        printf("->");
    }
    printf("\n");

    printf("backward: ");
    for(both_way_node* p=tail;p;p=p->pre){
        printf("%3d",p->val);
        printf("<-" );
    }
    printf("\n");
    clear_both_way(head);
}
int main(void){
    //test01();
    //test02();
    //test03();
    test04();
    system("pause");
    return 0;
}