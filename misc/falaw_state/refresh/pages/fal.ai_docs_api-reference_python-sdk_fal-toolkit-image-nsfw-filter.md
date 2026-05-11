> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# fal.toolkit.image.nsfw_filter

> API reference for fal.toolkit.image.nsfw_filter

```python theme={null}
from fal.toolkit.image.nsfw_filter import NSFWImageDetectionInput, NSFWImageDetectionOutput, run_nsfw_estimation
```

## Classes

### NSFWImageDetectionInput

```python theme={null}
class fal.toolkit.image.nsfw_filter.NSFWImageDetectionInput
```

!!! abstract "Usage Documentation" [Models](../concepts/models.md)

A base class for creating Pydantic models.

> **Inherits from:** `BaseModel`

<Accordion title="Constructor Parameters" defaultOpen>
  | Name   | Type  | Default | Description |
  | :----- | :---- | :------ | :---------- |
  | `data` | `Any` | -       | -           |
</Accordion>

<Accordion title="Class Variables" defaultOpen>
  | Name        | Type  | Default | Description |
  | :---------- | :---- | :------ | :---------- |
  | `image_url` | `str` | -       | -           |
</Accordion>

### NSFWImageDetectionOutput

```python theme={null}
class fal.toolkit.image.nsfw_filter.NSFWImageDetectionOutput
```

!!! abstract "Usage Documentation" [Models](../concepts/models.md)

A base class for creating Pydantic models.

> **Inherits from:** `BaseModel`

<Accordion title="Constructor Parameters" defaultOpen>
  | Name   | Type  | Default | Description |
  | :----- | :---- | :------ | :---------- |
  | `data` | `Any` | -       | -           |
</Accordion>

<Accordion title="Class Variables" defaultOpen>
  | Name               | Type    | Default | Description |
  | :----------------- | :------ | :------ | :---------- |
  | `nsfw_probability` | `float` | -       | -           |
</Accordion>

***

## Functions

### run\_nsfw\_estimation

```python theme={null}
def run_nsfw_estimation(input: fal.toolkit.image.nsfw_filter.inference.NSFWImageDetectionInput) -> fal.toolkit.image.nsfw_filter.inference.NSFWImageDetectionOutput
```

| Parameter | Type                      | Default | Description |
| :-------- | :------------------------ | :------ | :---------- |
| `input`   | `NSFWImageDetectionInput` | -       | -           |

**Returns:** `NSFWImageDetectionOutput`
