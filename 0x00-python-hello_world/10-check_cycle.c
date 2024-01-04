#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if list is cyclical
 * @list: pointer to list check
 * Return: 1if cyclical, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
