#include "lists.h"
#include <stdio.h>

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
	listint_t *ti = *head;
	char str[99999];
	size_t i, j, len = 0;

	if (head == NULL || *head == NULL)
		return (1);
	len = list_len(ti);
	for (i = 0; i < len; i++)
	{
		str[i] = ti->n;
		ti = ti->next;
	}
	i = 0;
	for (i = 0, j = len - 1; i < len; i++, j--)
	{
		if (str[i] != str[j])
		{
			return (0);
		}
	}
	return (1);
}
