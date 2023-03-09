#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for cycle in a linked list
 * @list: stores address of the first node
 * Return: Allow success
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	while (list)
	{
		while (tmp)
		{
			if (list == tmp->next)
				return (1);
			tmp = tmp->next;
		}
		tmp = list->next;
		list = list->next;
	}
	return (0);
}
