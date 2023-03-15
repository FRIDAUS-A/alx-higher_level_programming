#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: stores the address of the pointer to the first node
 * Return: Allow success
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *stop = NULL;

	if (*head == NULL)
		return (1);
	while ((*head)->next != stop)
	{
		while (tmp->next != stop)
		{
			tmp = tmp->next;
		}
		stop = tmp;
		if ((*head)->n != stop->n)
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
