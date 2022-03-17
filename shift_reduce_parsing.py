#include<bits/stdc++.h>
using namespace std;
unordered_map<string,string>m; // TO STORE THE LHS AND RHS OF PRODUCTIONS
void Productions(vector<string>&productions,int n)
{
    string s;
    cout<<"ENTER THE PRODUCTIONS"<<endl;
    while(n--)
    {
    cin>>s;
    productions.push_back(s);
    }
}
//s+(s-s)
bool f(string &a,vector<string>&stk1,vector<string>&A1,vector<string>&action1)
{
  int n = a.length();
  string curr = "";
  for(int i = n-1;i>=0;i--)
  {
      curr+=a[i];
      int len = curr.length();
      string t;
      for(int  j = len-1;j>=0;j--)
      {
           t.push_back(curr[j]);
           string rev= t;
           reverse(t.begin(),t.end());
           if(m.find(t)!=m.end())
           {
               int z = t.size();
               stk1.push_back(t);
               A1.push_back("$");
                while(z--)
               {
                curr.pop_back();
                t.pop_back();
               }
               string ans= "REDUCED  ";
               ans+=t;
               ans+="->";
               string sub = m[t];
               ans+=m[t];
               action1.push_back(ans);
               curr+=sub;
               len = curr.size();
               j = curr.size()-1;
           }
      }
  }
  return curr=="$E";
}
void Split_Productions(vector<string>&productions,int n)
{
    for(int i=0;i<n;i++)
    {
       string l,r;
       int len = productions[i].length();
       string temp = productions[i];
       int x = 0;
       while(x<len)
        {
           if(x+1<len && temp[x]=='-' && temp[x+1]=='>')
           {
                x = x + 2;
                break;
           }
           l.push_back(temp[x]);
           x++;
        }
        while(x<len)
        {
           r.push_back(temp[x]);
           x++;
        }
        m[r] = l;
    }
}
void print(vector<string>&v1,vector<string>&v2,vector<string>&v3)
{
    cout<<"STACK    "<<"I/P BUFFER  "<<"ACTION    "<<endl;
    for(int i = 0  ;i < v1.size() ; i++)
    {
        cout<<v1[i]<<"       "<<v2[i]<<"         "<<v3[i]<<endl;
    }
}
int main()
{
    int n;
    cout<<"ENTER THE NUMBER OF PRODUCTIONS:"<<endl;
    cin>>n;
    vector<string>productions;
    Productions(productions,n);
    Split_Productions(productions,n);
    
    cout<<"ENTER I/P BUFFER:"<<endl;
    string a;//THE STRING WHICH HAS TO GET REDUCED  TO THE START SYMBOL OF THE GRAMMAR
    cin>>a;
    n = a.length();
    string curr;
    curr.push_back('$'); //BY DEFAULT WE WILL PUSH THIS INTO THE STACK
    vector<string>stk;
    vector<string>A;
    vector<string>action;
    for(int i=0;i<n;i++)
    {
      curr.push_back(a[i]);
      string shift = "shift  ";
      shift.push_back(a[i]);
      string ans;
      stk.push_back(curr); //->1
      action.push_back(shift);//->3
      for(int  f = i;f<n;f++)
      {
           ans.push_back(a[f]);
      }
      A.push_back(ans);//->2  
      int  k = curr.size();
      string t;
      
       for(int  j=k-1;j>=0;j--)
      {
          t.push_back(curr[j]);
          string rev = t;
          reverse(rev.begin(),rev.end());
          if(m.find(rev)!=m.end())
          {
              
              A.push_back(A.back());//->2
              string R = "REDUCED  ";
              R+=  rev + "->" + m[rev]; 
              action.push_back(R);//->3
              string sub = m[rev];
              int p      = rev.size();
              while(p--)
              {
                  curr.pop_back();
                  t.pop_back();
              }
              curr+=sub;
              stk.push_back(curr);//->1
              k = curr.size();
              j = k-1;
          }
      }
    }
    cout<<curr;
    cout<<endl;
    print(stk,A,action);
    if(curr=="$A")
    {
    cout<<"ACCEPTED";
    return 0;
    }
    return 0;
}
