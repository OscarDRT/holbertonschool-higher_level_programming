#include "lists.h"

/**
 *list_len - Returns the number of elements in a linked list_t list
 * @h: contains the header of the list
 * Return: Number of nodes
 */
size_t list_len(listint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: head of th list
 * Return: 1 is palindrome or 0 is not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ti = *head, *ts = *head;
	size_t i = 1, j = 1, len = 0;

	if (head == NULL || *head == NULL)
		return (1);
	len = list_len(ti);
	while (i != len)
	{
		for (j = 1; j < len; j++)
			ti = ti->next;
		if (ti->n != ts->n)
		{
			return (0);
		}
		else
		{
			ts = ts->next;
			if (ti == ts)
				break;
			ti = *head;
			len--;
			i++;
		}
	}
	return (1);
}
