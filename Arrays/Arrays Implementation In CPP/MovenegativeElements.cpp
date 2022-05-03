#include <bits/stdc++.h> 
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++){   //Making an array
        cin>>arr[i];
    }
    int counter = 0;
    for (int i = 0; i < n; i++){
        if (arr[i] < 0){
            swap(arr[i],arr[counter]);
            counter++;
        }
    }
    for (int i = 0; i < n; i++){
        cout<<arr[i]<<endl;
    }
    return 0;
}