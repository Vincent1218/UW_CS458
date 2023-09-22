#include <stdio.h>
#include <stdlib.h>
#include <crypt.h>

int main() {
  char* cryptPass = crypt("password", "00");
  printf("%s", cryptPass); 
  return 0;
}
