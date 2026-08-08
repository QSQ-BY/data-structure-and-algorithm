//键值对，一个键只能对应一个值，一个值可以有多个键
//底层基于红黑树
/*
#include <map>
#include <unordered_map>
using namespace std;
//声明map
map<key_type,value_type> map_name

//插入元素
map_name[key] = value
map_name.insert(pair<key_type,value_type>(key,value))

//访问元素
value_type value = map_name[key]
//如果访问的键不存在则会创建一个新的键值对其中value被初始化为value_type的默认值

//删除元素
map_name.erase(key)

//查找元素
if(map_name.find(key) != map_name.end()){
    //找到元素
}else if(map_name.find(key) == map_name.end()){
    //没找到元素
}

//遍历元素
for(auto x:map_name){
    key_type key = x.first;
    value_type value = x.second; 
    //x是一个pair键值对
}

//获取map中键的元素个数
int size = map_name.size()

//判断map是否为空
if(map_name.empty()){
    //map为空
}else if(!map_name.empty()){
    //map不为空
}
*/
#include <iostream>
#include <map>
using namespace std;
int main(void){
    //声明一个存储字符串到整数的映射map
    map<string,int> word_count;

    //插入元素
    word_count["apple"] = 3;
    word_count["banana"] = 2;
    word_count["cherry"] = 3;

    //访问元素
    cout<<"number of apples: "<<word_count["apple"]<<endl;

    //遍历元素
    for(auto x:word_count){
        cout<<"numbers of "<<x.first<<" is "<<x.second<<endl;
    }

    //删除元素
    word_count.erase("banana");

    //map判空
    if(word_count.empty()){
        cout<<"map is empty"<<endl;
    }else{
        cout<<"map is not empty"<<endl;
    }

    //map元素数量
    cout<<"map中有"<<word_count.size()<<"个元素"<<endl;

    system("pause");
    return 0;
}

//unordered_map与map的区别在于
/* map会对键进行自动排序前者则不会
且unordered_map的底层基于哈希表进行实现
查询时间复杂度为O1，后者则为O（logn） */