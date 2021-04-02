#include<iostream>
#include<string.h>
using namespace std;
char encoded(string s , char arr[]){
    int lo = 0;
    int hi = 15;
    int mid = 7;
    for (auto c : s){
        if (c == '0'){
            hi = mid;
            mid = (lo + hi)/2;
        }
        else{
            lo = mid;
            mid = (lo+hi)/2;
        }
    }
    return arr[hi];

}
int main(){
    int test_cases = 0;
    cin>>test_cases;
    while(test_cases){
        char alphabets [16] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'};
        int n;
        cin>>n;
        string s = "";
        cin>>s;
        string decoded = "";
        int lo = 0;
        int hi = 4;

        while(n){
            decoded += encoded(s.substr(lo,hi),alphabets);
            lo += 4;
            n -= 4;
        }
        cout<<decoded<<endl;
        
        test_cases -= 1;
    }
    return 0;
}