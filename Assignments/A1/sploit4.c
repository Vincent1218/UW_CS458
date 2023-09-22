#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
  char *token, *script;
  FILE *fp;
  char pw[200];

  setenv("HOME","/root",1);
  system("/usr/local/bin/pwgen -w > temp.txt");
  fp = fopen("temp.txt", "r");
  fscanf(fp, "%[^\n]", pw);
  token = strtok(pw, ":");
  token = strtok(NULL, ":");
  token = strtok(token, " ");
  fclose(fp);
  sprintf(script,"expect -c 'spawn su root; expect \"Password:\"; send \"%s\\r\"; interact'", token);
  system(script);
  system("rm temp.txt");
  return 0;
}
