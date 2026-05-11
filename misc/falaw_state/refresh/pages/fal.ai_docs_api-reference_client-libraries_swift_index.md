> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Swift Client

> fal client library for iOS, macOS, tvOS, and watchOS

The `fal-swift` package provides a native Swift interface for calling fal AI models on Apple platforms.

## Installation

Add the package via Swift Package Manager:

```swift theme={null}
.package(url: "https://github.com/fal-ai/fal-swift.git", from: "0.5.6")
```

## Quick Start

```swift theme={null}
import FalClient

let result = try await fal.subscribe(
    to: "fal-ai/flux/dev",
    input: [
        "prompt": "a cat",
        "seed": 6252023,
        "image_size": "landscape_4_3",
        "num_images": 4
    ],
    includeLogs: true
) { update in
    if case let .inProgress(logs) = update {
        print(logs)
    }
}
```

## Supported Platforms

* iOS 16+
* macOS 13+
* tvOS 16+
* watchOS 9+

## API Reference

<Card title="Swift API Reference" icon="book" href="https://swiftpackageindex.com/fal-ai/fal-swift/documentation/falclient">
  Full API documentation on Swift Package Index
</Card>

<Card title="GitHub Repository" icon="github" href="https://github.com/fal-ai/fal-swift">
  Source code and examples
</Card>
