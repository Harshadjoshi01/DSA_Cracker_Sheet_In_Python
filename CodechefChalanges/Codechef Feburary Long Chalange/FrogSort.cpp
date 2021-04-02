#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int subtask_1(int weights[], int jumps[]){
    int re = 0;
    if (weights[0] == 2){
        if(jumps[0] >= 2){
            re = 1;
        } else {
            re = 2;
        }
    }
    return re;
}

int find_index(int weights[],int size, int value){
    for (int i = 0; i < size; i++){
        if (weights[i] == value){
            return i;
        }
    }
    return -1;
}

int jump(int require_jump, int actual_jump){
    int jumps = 0;
    if (actual_jump >= require_jump){
        jumps = 1;
    } else {
        int z = require_jump & 1;
        if (z==0){
            jumps = require_jump/actual_jump;
        } else {
            jumps = (require_jump/actual_jump) + 1;
        }
    }

    return jumps;
}

int main(){
    int test_case;
    cin>>test_case;
    while(test_case){
        int n;
        cin>>n;
        int weights[n];
        int jumps[n];
        int result = 0;
        for(int i = 0; i < n; i++){
            cin>>weights[i];
        }
        for(int i = 0; i < n; i++){
            cin>>jumps[i];
        }
        if (n == 2){
            result = subtask_1(weights,jumps);
        } else {
            int index = find_index(weights,n,1);
            int x = 2;
            int jump_count = 0;
            while(x<=n){
                int i = find_index(weights,n,x);
                int value = index - i;
                if (value >= 0){
                    int require_jump = value + 1;
                    int j = jump(require_jump,jumps[i]);
                    index = i + (j * jumps[i]);
                    jump_count += j;
                    x++;

                } else {
                    index = i;
                    x++;
                }
            }
            result = jump_count;
        } 
        cout<<result<<endl;
        test_case--;
    }
    return 0;
}