// ConsoleApplication1.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int>a, pair<int, int>b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    else {
        return a.second > b.second;
    }
}

int main()
{
    int N, K;
    cin >> N >> K;
    vector<pair<long long int,long long int>> jLt;
	for(int i = 0;i<N;i++)
	{
        long long int m, v;
        cin >> m >> v;
        jLt.push_back({m,v});
	}
    sort(jLt.begin(), jLt.end(), compare);
    /*cout << "---------" << endl;
    for (int i = 0; i < N; i++)
    {
        cout << jLt[i].first << " " << jLt[i].second << endl;
    }*/
    
	
    multiset<long long int> blt;

	for (int i = 0;i<K;i++)
	{
        int g;
        cin >> g;
        blt.insert(g);
	}
	
    long long int V = 0;
    for (int i = 0; i < N; i++)
    {
    	if(blt.empty())
    	{
            break;
    	}
        long long int m = jLt[i].first;
        long long int v = jLt[i].second;
        multiset<long long int>::iterator l = blt.lower_bound(m);
        if(l!=blt.end())
        {
            V += v;
            blt.erase(l);
        }
    }
    cout << V << endl;
}
