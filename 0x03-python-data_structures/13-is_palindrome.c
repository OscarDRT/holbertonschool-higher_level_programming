#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: head of th list
 * Return: 1 is palindrome or 0 is not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ti = *head, *ts = *head;
	int i = 1, j = 1, len = 0;

	if (head == NULL || *head == NULL)
		return (1);
	while (ti)
	{
		len++;
		ti = ti->next;
	}
	ti = *head;
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
