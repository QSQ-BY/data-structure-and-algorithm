#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define cmp <
#define ROOT 1
#define FATHER(i) ((i)/(2))
#define LEFT(i) ((i)*(2))
#define RIGHT(i) ((i)*(2)+(1))


typedef struct node{
    char ch;
    int freq;
    struct node *lchild,*rchild;
}node;
//堆结构
typedef struct heap{
    node** __data;
    node** data;
    int cnt;
    int size;
}heap;

//交换节点数组中的i位置和j位置的值
void swap(node** arr,int i ,int j){
    node* temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    return;
}

//堆结构的操作
heap* get_new_heap(int size){
    heap* h = (heap*)malloc(sizeof(heap));
    h->__data = (node**)malloc(sizeof(node*)*size);
    h->data = h->__data-1;
    h->cnt = 0;
    h->size = size;
    return h;
}

//小顶堆
//压入操作
int full(heap* h){
    if(h==nullptr) return 0;
    return h->cnt == h->size;
}

int empty(heap* h){
    if(h == nullptr) return 1;
    return h->cnt == 0;
}

node* top(heap* h){
    if(h==nullptr) return nullptr;
    if(h->cnt == 0) return nullptr;
    return h->data[1];
}

void up_update(heap* h,int i){
    while(i>1){
        if(h->data[i]->freq cmp h->data[FATHER(i)]->freq){
            swap(h->data,i,FATHER(i));
        }else break;
        i = FATHER(i);
    }
    return;
}

void down_update(heap* h,int i,int n){
    int index = i;
    while(LEFT(i)<=n){
        index = i;
        if(h->data[i]->freq > h->data[LEFT(i)]->freq) index = LEFT(i);
        if(RIGHT(i)<=n and h->data[index]->freq > h->data[RIGHT(i)]->freq) index = RIGHT(i);
        if(index == i) break;
        swap(h->data,index,i);
        i=index;
    }
    return;
}

int push_heap(heap* h, node* n){
    if(h==nullptr or full(h)) return 0;
    h->cnt++;
    h->data[h->cnt] = n;
    up_update(h,h->cnt);
    return 1;
}

int pop_heap(heap* h){
    if(empty(h)) return 0;
    h->data[1] = h->data[h->cnt];
    h->cnt--;
    down_update(h,1,h->cnt);
    return 1;
}


void clear(heap* h){
    if(h==nullptr) return;
    free(h->__data);
    free(h);
    return;
}

node* get_new_node(int freq,char ch){
    node* p = (node*)malloc(sizeof(node));
    p->ch = ch;
    p->freq = freq;
    p->lchild = p->rchild = nullptr;
    return p;
}

/* void swap(node** arr,int i ,int j){
    node* temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    return;
} */

int find_min_node(node** node_arr,int n){
    int index = 0;
    for(int i = 0;i<=n;i++){
        if(node_arr[i]->freq < node_arr[index]->freq){
            index = i;
        }
    }
    return index;
}

node* build_huffman_tree(node** node_arr,int n){

    for(int i =1;i<n;i++){
        int min_index1 = 0;
        int min_index2 = 0;
        min_index1 = find_min_node(node_arr,n-i);
        swap(node_arr,min_index1,n-i);
        min_index2 = find_min_node(node_arr,n-1-i);
        swap(node_arr,min_index2,n-i-1);
        int new_freq = node_arr[n-i]->freq + node_arr[n-i-1]->freq;
        node* new_node = get_new_node(new_freq,0);
        new_node->lchild = node_arr[n-i-1];
        new_node->rchild = node_arr[n-i];
        node_arr[n-i-1] = new_node;
    }
    return node_arr[0];
}


node* build_huffman_tree_heap(node** node_arr,int n){
    if(n<=0 or node_arr == nullptr) return nullptr;
    heap* h = get_new_heap(n);
    for(int i =0;i<n;i++){
        push_heap(h,node_arr[i]);
    }
    for(int i =1;i<n;i++){
        node* node1 = top(h);
        pop_heap(h);
        node* node2 = top(h);
        pop_heap(h);
        node* new_node = get_new_node(node1->freq+node2->freq,0);
        new_node->lchild = node1;
        new_node->rchild = node2;
        push_heap(h,new_node);
    }
    node* ret = top(h);
    clear(h);
    return ret;
}

void extract_huffman_code(node* root , char* buff ,int k){
    if(root == nullptr) return;
    buff[k] = 0;
    if(root->lchild == nullptr and root->rchild == nullptr){
        if(k == 0){
            buff[k++] = '0';
            buff[k] = 0;
        }
        printf("%c:%s\n", root->ch, buff);
        return;
    }
    if(root->lchild){
        buff[k] = '0';
        extract_huffman_code(root->lchild,buff,k+1);
    }
    if(root->rchild){
        buff[k] = '1';
        extract_huffman_code(root->rchild, buff , k+1);
    }
    return;
}

int get_wpl(node* root,int depth){
    if(root == nullptr) return 0;
    if(root->lchild == nullptr and root->rchild == nullptr){
        return root->freq * depth;
    }
    return get_wpl(root->lchild,depth+1) + get_wpl(root->rchild,depth+1);
}

int get_leaf_count(node* root){
    if(root == nullptr) return 0;
    if(root->lchild == nullptr and root->rchild == nullptr) return 1;
    return get_leaf_count(root->lchild) + get_leaf_count(root->rchild);
}

void clear_tree(node* root){
    if(root == nullptr) return;
    clear_tree(root->lchild);
    clear_tree(root->rchild);
    free(root);
    return;
}

void run_huffman_case(int case_id,const char* name,const char* chars,const int* freq,int n,int expected_root,int expected_wpl,int expected_leaf){
    node** node_arr = nullptr;
    if(n > 0){
        node_arr = (node**)malloc(sizeof(node*)*n);
        for(int i=0;i<n;i++){
            node_arr[i] = get_new_node(freq[i],chars[i]);
        }
    }

    node* root = build_huffman_tree_heap(node_arr,n);
    int root_freq = root ? root->freq : 0;
    int wpl = get_wpl(root,0);
    int leaf_count = get_leaf_count(root);
    int pass = (root_freq == expected_root and wpl == expected_wpl and leaf_count == expected_leaf);

    printf("| %4d | %-12s | %3d | %8d | %8d | %4d | %-4s |\n",
           case_id,name,n,root_freq,wpl,leaf_count,pass ? "OK" : "FAIL");

    printf("  Codes for %s:\n",name);
    if(root == nullptr){
        printf("  (empty)\n");
    }else{
        char buff[1000];
        extract_huffman_code(root,buff,0);
    }

    clear_tree(root);
    free(node_arr);
    return;
}

void test01(){
    int single_freq[] = {5};
    int two_freq[] = {5,7};
    int classic_freq[] = {5,9,12,13,16,45};
    int same_freq[] = {2,2,2,2};
    int normal_freq[] = {1,2,3,4,5};

    printf("+------+--------------+-----+----------+----------+------+------+\n");
    printf("| Case | Name         |   n | RootFreq |      WPL | Leaf | Pass |\n");
    printf("+------+--------------+-----+----------+----------+------+------+\n");

    run_huffman_case(1,"empty","",nullptr,0,0,0,0);
    run_huffman_case(2,"single","A",single_freq,1,5,0,1);
    run_huffman_case(3,"two","AB",two_freq,2,12,12,2);
    run_huffman_case(4,"classic","ABCDEF",classic_freq,6,100,224,6);
    run_huffman_case(5,"same freq","ABCD",same_freq,4,8,16,4);
    run_huffman_case(6,"normal","ABCDE",normal_freq,5,15,33,5);

    printf("+------+--------------+-----+----------+----------+------+------+\n");
    return;
}
int main(void){
    srand(time(0));
    test01();
    system("pause");
    return 0;
}