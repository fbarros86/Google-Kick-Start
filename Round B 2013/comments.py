import sys


'''

Input

//*no recursion*/* file header
***********/************
* Sample input program *
**********/*************
*/
int spawn_workers(int worker_count) {
  /* The block below is supposed to spawn 100 workers.
     But it creates many more.
     Commented until I figure out why.
  for (int i = 0; i < worker_count; ++i) {
    if(!fork()) {
      /* This is the worker. Start working. */
      do_work();
    }
  }
  */
  return 0; /* successfully spawned 100 workers */
}

int main() {
  printf("Hello /*a comment inside string*/ world");
  int worker_count = 0/*octal number*/144;
  if (spawn_workers(worker_count) != 0) {
    exit(-1);
  }
  return 0;
}


Output

Case #1:
/* file header
************************
*/
int spawn_workers(int worker_count) {

  return 0;
}

int main() {
  printf("Hello  world");
  int worker_count = 0144;
  if (spawn_workers(worker_count) != 0) {
    exit(-1);
  }
  return 0;
}

'''

count = 0
res = ""
for line in sys.stdin:
    x=0
    while x<(len(line)):
        if (line[x]=='/' and line[x+1]=='*'):
            count+=1
            x+=1
        elif (count==0):res += line[x]
        elif (line[x]=='*' and line[x+1]=='/'):
            count-=1
            x+=1
        x+=1
print("Case 1#:")
print(res, end='')
