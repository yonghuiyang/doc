#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>

int main()
{
  clock_t start = clock();//返回进程从开始到现在的微秒数
  printf("%d, %d\n", start, CLOCKS_PER_SEC);
  
  time_t timep;
  int timestamp = time(&timep);
  printf("%d\n", timestamp);
  struct tm *p;
  p = localtime(&timep); //可以完成时间的加减
  printf("%d%d%d\n", (1900 + p->tm_year), (1 + p->tm_mon), p->tm_mday);
  
  struct timeval tv;
  struct timezone tz;
  gettimeofday(&tv, &tz);
  printf("tv_sec: %d, tv_usec: %d\n", tv.tv_sec, tv.tv_usec);
}
