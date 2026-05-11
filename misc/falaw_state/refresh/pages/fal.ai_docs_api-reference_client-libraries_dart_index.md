> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dart Client

> fal client library for Flutter applications

The `fal_client` package provides a Dart interface for calling fal AI models in Flutter applications.

## Installation

```bash theme={null}
flutter pub add fal_client
```

## Quick Start

```dart theme={null}
import 'package:fal_client/fal_client.dart';

final fal = FalClient.withCredentials("YOUR_FAL_KEY");

final result = await fal.subscribe("fal-ai/flux/dev", input: {
  "prompt": "a cat",
  "seed": 6252023,
  "image_size": "landscape_4_3",
  "num_images": 4
});

print(result);
```

## Supported Platforms

* Flutter (iOS, Android, Web, Desktop)
* Dart (standalone)

## API Reference

<Card title="Dart API Reference" icon="book" href="https://pub.dev/documentation/fal_client/latest">
  Full API documentation on pub.dev
</Card>

<Card title="GitHub Repository" icon="github" href="https://github.com/fal-ai/fal-dart">
  Source code and examples
</Card>

<Card title="Example App" icon="mobile" href="https://pub.dev/packages/fal_client/example">
  Simple Flutter app using fal image inference
</Card>
