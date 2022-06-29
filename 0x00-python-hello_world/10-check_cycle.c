#include "lists.h"
#include <stdio.h>
/**
* check_cycle - check if a singly linked list
* @list: the singly linked list is schecked
*
* Return: 1 if has a cycle in it or 0 if not
*/
int check_cycle(listint_t *list)
{
listint_t *tee = list, *hee = list;
int found = 0;
while ((tee && hee) && hee->next)
{
tee = tee->next;
if (hee->next || hee->next->next;
else
break;
if (tee == hee)
{
found = 1;
break;
}
}
return (found);
