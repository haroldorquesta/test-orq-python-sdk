# Deployments

The deployment request payload


## Fields

| Field                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                     | The deployment id to invoke                                                                                                                                                                                            |
| `stream`                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | If set, partial message content will be sent. Tokens will be sent as data-only `server-sent events` as they become available, with the stream terminated by a `data: [DONE]` message.                                  |
| `inputs`                                                                                                                                                                                                               | Dict[str, [models.Inputs](../models/inputs.md)]                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used.                                                                     |
| `context`                                                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key.                              |
| `prefix_messages`                                                                                                                                                                                                      | List[[models.PrefixMessages](../models/prefixmessages.md)]                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                     | A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment.                                                                                  |
| `messages`                                                                                                                                                                                                             | List[[models.Messages](../models/messages.md)]                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                     | A list of messages to send to the deployment.                                                                                                                                                                          |
| `file_ids`                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                     | A list of file IDs that are associated with the deployment request.                                                                                                                                                    |
| `metadata`                                                                                                                                                                                                             | Dict[str, *Any*]                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | Key-value pairs that you want to attach to the log generated by this request.                                                                                                                                          |
| `chain_id`                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Unique ID that identifies a chaining operation. This is useful for tracking a chain of completions across multiple                                                                                                     |
| `conversation_id`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Unique ID that identifies a chat conversation. This is useful for tracking the same conversation across multiple requests                                                                                              |
| `user_id`                                                                                                                                                                                                              | [Optional[models.UserID]](../models/userid.md)                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                     | Unique ID that identifies a user. This is useful for tracking the same user across multiple requests                                                                                                                   |
| `deployment_id`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Unique ID that identifies a deployment entity.                                                                                                                                                                         |
| `deployment_variant_id`                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                     | Unique ID that identifies a specific variant of a deployment.                                                                                                                                                          |
| `extra_params`                                                                                                                                                                                                         | Dict[str, *Any*]                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration. |
| `invoke_options`                                                                                                                                                                                                       | [Optional[models.InvokeOptions]](../models/invokeoptions.md)                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                    |