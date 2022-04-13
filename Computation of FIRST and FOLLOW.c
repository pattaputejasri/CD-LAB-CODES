#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
#include&lt;conio.h&gt;
#define max 20
char prod[max][10];
char ter[10],nt[10];
char first[10][10],follow[10][10];
int eps[10];
int count=0;
int findpos(char ch)
{
int n;
for(n=0;nt[n]!=&#39;\0&#39;;n++)
if(nt[n]==ch)
break;
if(nt[n]==&#39;\0&#39;)
return 1;

return n;
}
int IsCap(char c)
{
if(c &gt;= &#39;A&#39; &amp;&amp; c&lt;= &#39;Z&#39;)
return 1;
return 0;
}
void add(char *arr,char c)
{
int i,flag=0;
for(i=0;arr[i]!=&#39;\0&#39;;i++)
{
if(arr[i] == c)
{
flag=1;
break;
}
}
if(flag!=1)
arr[strlen(arr)] = c;
}void addarr(char *s1,char *s2)
{
int i,j,flag=99;
for(i=0;s2[i]!=&#39;\0&#39;;i++)
{
flag=0;
for(j=0;;j++)
{
if(s2[i]==s1[j])
{
flag=1;
break;
}
if(j==strlen(s1) &amp;&amp; flag!=1)
{
s1[strlen(s1)] = s2[i];
break;
}
}
}
}
void addprod(char *s)
{
int i;
prod[count][0] = s[0];
for(i=3;s[i]!=&#39;\0&#39;;i++)
{
if(!IsCap(s[i]))
add(ter,s[i]);
prod[count][i-2] = s[i];
}

prod[count][i-2] = &#39;\0&#39;;
add(nt,s[0]);
count++;
}
void findfirst()
{
int i,j,n,k,e,n1;
for(i=0;i&lt;count;i++)
{
for(j=0;j&lt;count;j++)
{n = findpos(prod[j][0]);
if(prod[j][1] == (char)238)
eps[n] = 1;
else
{
for(k=1,e=1;prod[j][k]!=&#39;\0&#39; &amp;&amp; e==1;k++)
{
if(!IsCap(prod[j][k]))
{
e=0;
add(first[n],prod[j][k]);
}
else
{
n1 = findpos(prod[j][k]);
addarr(first[n],first[n1]);
if(eps[n1] == 0)
e=0;
}
}
if(e==1)
eps[n]=1;
}
}
}
}
void findfollow()
{
int i,j,k,n,e,n1;
n = findpos(prod[0][0]);
add(follow[n],&#39;$&#39;);
for(i=0;i&lt;count;i++)
{
for(j=0;j&lt;count;j++)
{
k = strlen(prod[j])-1;
for(;k&gt;0;k--)
{
if(IsCap(prod[j][k]))
{
n=findpos(prod[j][k]);
if(prod[j][k+1] == &#39;\0&#39;) // A -&gt; aB{

n1 = findpos(prod[j][0]);
addarr(follow[n],follow[n1]);
}
if(IsCap(prod[j][k+1])) // A -&gt; aBb
{
n1 = findpos(prod[j][k+1]);
addarr(follow[n],first[n1]);
if(eps[n1]==1)
{
n1=findpos(prod[j][0]);
addarr(follow[n],follow[n1]);
}
}
else if(prod[j][k+1] != &#39;\0&#39;)
add(follow[n],prod[j][k+1]);
}
}
}
}
}
void main()
{
char s[max],i;
printf(&quot;\nEnter the productions(type &#39;end&#39; at the last of the
production)\n&quot;);
scanf(&quot;%s&quot;,s);
while(strcmp(&quot;end&quot;,s))
{ addprod(s);
scanf(&quot;%s&quot;,s);}
findfirst();
findfollow();
printf(&quot;Non-Terminals\t FIRST\t FOLLOW\n&quot;);
for(i=0;i&lt;strlen(nt);i++)
{ printf(&quot;%c\t\t&quot;,nt[i]);
printf(&quot;%s&quot;,first[i]);
if(eps[i]==1)
printf(&quot;%c\t\t&quot;,(char)238);
else
printf(&quot;\t&quot;);
printf(&quot;%s-{e}\n&quot;,follow[i]);}
getch();
}
