# Django Marketplace Conversation App

This document provides an overview and explanation of the features and functionality for the conversation system within a Django marketplace application.

## Features

### 1. Start a New Conversation
- **Functionality**: Users can start a new conversation about an item.
- **Behavior**:
  - If the item belongs to the user, they are redirected to their dashboard.
  - If a conversation already exists for the item with the user, they are redirected to the existing conversation detail page.
  - Users can send an initial message when starting a new conversation.

### 2. Inbox View
- **Functionality**: Users can view all their conversations.
- **Behavior**:
  - The inbox lists all conversations involving the user.
  - Each conversation preview includes the latest message and the user who sent it.

### 3. Conversation Detail View
- **Functionality**: Users can view the details of a conversation.
- **Behavior**:
  - Users can see all messages exchanged in the conversation.
  - Users can send new messages within the conversation.

### 4. Conversation Models
- **Conversation**: Represents a conversation between users about an item.
  - Fields: `item`, `members`, `created_at`, `modified_at`.
- **ConversationMessage**: Represents a message within a conversation.
  - Fields: `conversation`, `content`, `created_at`, `created_by`.

### 5. Admin Configuration
- **Functionality**: Conversations and messages are registered in the admin interface for management.
- **Behavior**:
  - Admins can manage conversations and messages from the Django admin dashboard.

### 6. Forms
- **ConversationMessageForm**: Form for creating a new conversation message.
  - Fields: `content`.

## URLs and Views

### URLs
- **Inbox**: The inbox view is accessible via the root URL of the conversation app.
- **New Conversation**: Starting a new conversation is accessible via `/conversations/<item_pk>/`.
- **Conversation Detail**: Viewing a conversation detail is accessible via `/<int:pk>/`.

### Views
- **Inbox View**: Lists all conversations for the logged-in user.
- **New Conversation View**: Handles starting a new conversation and sending the initial message.
- **Conversation Detail View**: Displays all messages in a conversation and allows sending new messages.

## Templates

### `detail.html`
- Displays the conversation messages and a form to send new messages.
- Each message shows the sender and the timestamp.

### `inbox.html`
- Lists all conversations with previews of the latest message.
- Includes a link to view the full conversation.

### `new.html`
- Provides a form to start a new conversation.
- Allows the user to send the initial message.

## Summary

The Django Marketplace Conversation App enables users to communicate about items through conversations. It includes views for managing conversations, templates for displaying conversation data, and models for storing conversation details. Admin functionality is also provided for managing conversations and messages.
