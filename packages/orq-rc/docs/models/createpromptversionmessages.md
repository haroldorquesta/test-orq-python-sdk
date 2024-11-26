# CreatePromptVersionMessages


## Fields

| Field                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `role`                                                                                                                                                                                                                                                                   | [models.CreatePromptVersionRole](../models/createpromptversionrole.md)                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                                       | The role of the prompt message                                                                                                                                                                                                                                           |
| `content`                                                                                                                                                                                                                                                                | [models.CreatePromptVersionContent](../models/createpromptversioncontent.md)                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                       | The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts.  |
| `tool_calls`                                                                                                                                                                                                                                                             | List[[models.CreatePromptVersionToolCalls](../models/createpromptversiontoolcalls.md)]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                      |