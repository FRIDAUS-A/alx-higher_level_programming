#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	int *tmp = list;

	while (list)
	{
		if (list == tmp)
			return (1);
		list = (*list).next;
	}
	return (0);
}
