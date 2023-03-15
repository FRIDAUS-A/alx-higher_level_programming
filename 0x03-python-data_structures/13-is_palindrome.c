#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: stores the address of the pointer to the first node
 * Return: Allow success
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *stop;

	if (*head == NULL)
		return (1);
	while (*head)
		*head = (*head)->next;
	stop = *head;
	*head = tmp;
	while ((*head)->next != stop)
	{
		while (tmp->next != stop)
			tmp = tmp->next;
		stop = tmp;
		if ((*head)->n != stop->next->n)
			return (0);
		tmp = (*head)->next;
		*head = (*head)->next;
	}
	return (1);
}
