#include<iostream>
#include<algorithm>
using namespace std;
int sumArray(int arr[], int size){
    int sum = 0;
    for(int i = 0; i < size; i++){
        sum += arr[i]; 
    }
    return sum;
}
int main(){
    int test_cases = 0;
    cin>>test_cases;
    while(test_cases){
        int n,m;
        cin>>n>>m;
        int arr_john[n];
        int arr_jackson[m];
        for(int i = 0; i < n; i++){
            cin>>arr_john[i];
        }
        for(int i = 0; i < m; i++){
            cin>>arr_jackson[i];
        }
        int min_swap = 0;
        int temp = 0;
        bool print = true;
        int sum_votes_john = sumArray(arr_john,n);
        int sum_votes_jackson = sumArray(arr_jackson,m);
        while(sum_votes_john <= sum_votes_jackson){
            sort(arr_john, arr_john+n);
            sort(arr_jackson, arr_jackson+m);
            if (arr_john[0] < arr_jackson[m-1]){
                temp = arr_jackson[m-1];
                arr_jackson[m-1] = arr_john[0];
                arr_john[0] = temp;
                sum_votes_john = sumArray(arr_john,n);
                sum_votes_jackson = sumArray(arr_jackson,m);
                min_swap++;

            }
            else{
                print = false;
                cout<<-1<<endl;
                break;
            }
        }
        if (print == true){
            cout<<min_swap<<endl;
        }
        test_cases -= 1;
    }
    return 0;
}
