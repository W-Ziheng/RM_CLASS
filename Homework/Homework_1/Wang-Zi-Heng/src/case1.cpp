#include <iostream>
using namespace std;

int main() { // 主函数入口
    cout<<"Welcome to RM!"<< std::endl; // 输出 "Welcome to RM!" 到标准输出，并换行

    // 此处若头文件无 声明 std 需要在每个函数前标注
    // std::cout<<"Welcome to RM!"<< std::endl; // 使用 std 命名空间下的 cout 进行输出，并换行

    return 0; // 返回 0，表示程序正常结束
}