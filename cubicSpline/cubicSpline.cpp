#include<bits/stdc++.h>
using namespace std;
#define SIZE 50

struct D
{
    long double x, y;
};

D data[ SIZE ];
long double A[ SIZE ][ SIZE ], X[ SIZE ][ SIZE ], EPS[ SIZE ];
int minEPS = 15;

void Setup()
{
    for(int i = 0; i < 45; i++)
        cin >> data[ i ].x >> data[ i ].y;

    for(int i = 0; i < 45; i++)
        for(int j = 0; j < 45; j++)
            A[ i ][ j ] = X[ i ][ j ] =  0.0;
}

// Sum in matrix, ex: Sum xi, Sum xi^2 or Sum yi*xi^4, etc
long double Sum(D d[SIZE], int power, int forX)
{
    long double ans = 0.0;
    for(int i = 0; i < 45; i++)
    {
        if(forX)
            ans += pow(d[ i ].x, power);
        else ans += d[ i ].y * pow(d[ i ].x, power);
    }
    return ans;
}

// Put xi into poly to get value of Pm(xi)
long double GetY(long double a[SIZE][SIZE], D d[SIZE], int now, int index)
{
    long double ans = a[ now ][ 0 ];
    for(int i = 1; i <= now+15; i++)
        ans += a[ now ][ i ] * pow(d[ index ].x, i);

    return ans;
}

int main()
{
    Setup();
    for(int times = 15; times < 45; times++)
    {
        //cout << "---- [ A |B] matrix ----" << endl << endl;
        //cout << " [A] " << endl;
        // Build A matrix
        for(int i = 0; i <= times; i++)
        {
            for(int j = 0; j <= times; j++)
            {
                A[ i ][ j ] = Sum(data, i+j, 1);
                //cout << A[ i ][ j ] << " ";
            }
            //cout << endl;
        }
        A[ 0 ][ 0 ] = 45.0;
        //cout << endl;


        //cout << " [B] " << endl;
        // Build B matrix
        for(int i = 0; i <= times; i++)
        {
            A[ i ][ times+1 ] = Sum(data, i, 0);
            //cout << A[ i ][ times+1 ] << " ";
        }
        //cout << endl << endl;

        // Now have [ A |B] matrix, use Guassian Jordan Elimination
        for(int i = 0; i <= times; i++)
        {
            for(int j = 0; j <= times; j++)
            {
                if(j != i)
                {
                    long double cal = A[ j ][ i ] / A[ i ][ i ];
                    for(int k = 0; k <= times+1; k++)
                        A[ j ][ k ] -= cal * A[ i ][ k ];
                }
            }
        }

        // Cal Pm(x)'s coef
        cout << "---- Degree of Pm(x) ---- " << times << endl;
        cout << "Coef [";
        for(int i = 0; i <= times; i++)
        {
            X[ times-15 ][ i ] = A[ i ][ times+1 ] / A[ i ][ i ];
            if(i!=times)cout << X[ times-15 ][ i ] << ", ";
            else cout << X[ times-15 ][ i ];
            //cout << "Coef [ a" << i << " ] = " << X[ times-15 ][ i ] << endl;
        }
        cout << "]" << endl;
        cout << endl;

        // Print poly
        cout << X[ times-15 ][ 0 ];
        for(int i = 1; i <= times; i++)
        {
            if(X[ times-15 ][ i ] > 0)
                cout << "+" << X[ times-15 ][ i ] << "x^" << i;
            else  cout << X[ times-15 ][ i ] << "x^" << i;
        }
        cout << endl;

        // Standard derivation cal, same as eps cal
        int free = 45 - times;
        long double tmp;
        for(int i = 0; i < 45; i++)
        {
            tmp = GetY(X, data, times-15, i) - data[ i ].y;
            EPS[ times ] += pow(tmp, 2);
        }

        EPS[ times ] = sqrt(EPS[ times ] / free);
        cout << "Eps [ " << times << " ]  = " << EPS[ times ] << endl << endl;

        if(EPS[ times ] < EPS[ minEPS ])
            minEPS = times;
    }

    cout << endl << "---- The smallest eps in all poly is degree [ " << minEPS << " ] ----" << endl;
    cout << "Value = " << EPS[ minEPS ] << endl;
}