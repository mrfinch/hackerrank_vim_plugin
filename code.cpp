#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
//#include <cstring>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    //fgsrhd
	int t;
    cin >> t;
    while(t){
        int n;
        cin >> n;
        vector<int> a(n);
        int i=0;
        while(i<n){
            cin >> a[i];
            i++;
        }
        int mx=a[0];
        int curr=a[0];
        for(int i=1;i<n;i++){
            //curr=max(curr,curr+a[i]);
            curr=curr+a[i];
            if(curr<0){
                curr=0;
            }
            mx=max(curr,mx);    
        }
        bool all_neg=true;
        int mn=-11111;
        for(int i=0;i<n;i++){
           if(a[i]>=0){
               all_neg=false;
               break;
           } 
           if(a[i]>mn){
                mn=a[i];   
           }
        }
        if(all_neg){
            cout << mn << " ";    
        }
        else{
            cout << mx << " ";
        }
        if(all_neg){
            cout << mn << endl;     
        }
        else{
            mn=0;
            for(int i=0;i<n;i++){
                if(a[i]>0){
                    mn+=a[i];
                }               
            }
            cout << mn << endl;
        }
        t--;
    }
//adfsf
    return 0;
}

