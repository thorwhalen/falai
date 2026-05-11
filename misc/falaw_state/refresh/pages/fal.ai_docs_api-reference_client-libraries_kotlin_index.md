> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kotlin / Java Client

> fal client library for Android and JVM applications

The `fal-client` packages provide Kotlin and Java interfaces for calling fal AI models on Android and JVM platforms.

## Installation

<CodeGroup>
  ```groovy Gradle (Kotlin) theme={null}
  implementation 'ai.fal.client:fal-client-kotlin:0.7.1'
  ```

  ```groovy Gradle (Java) theme={null}
  implementation 'ai.fal.client:fal-client:0.7.1'
  ```

  ```xml Maven (Kotlin) theme={null}
  <dependency>
    <groupId>ai.fal.client</groupId>
    <artifactId>fal-client-kotlin</artifactId>
    <version>0.7.1</version>
  </dependency>
  ```

  ```xml Maven (Java) theme={null}
  <dependency>
    <groupId>ai.fal.client</groupId>
    <artifactId>fal-client</artifactId>
    <version>0.7.1</version>
  </dependency>
  ```
</CodeGroup>

<Note>
  **Java Async Support**

  If your code relies on asynchronous operations via `CompletableFuture` or `Future`, use the `ai.fal.client:fal-client-async` artifact instead.
</Note>

## Quick Start

<CodeGroup>
  ```kotlin Kotlin theme={null}
  import ai.fal.client.kt

  val fal = createFalClient()

  val input = mapOf<String, Any>(
      "prompt" to "a cat",
      "seed" to 6252023,
      "image_size" to "landscape_4_3",
      "num_images" to 4
  )
  val result = fal.subscribe("fal-ai/flux/dev", input, options = SubscribeOptions(
      logs = true
  )) { update ->
      if (update is QueueStatus.InProgress) {
          println(update.logs)
      }
  }
  ```

  ```java Java theme={null}
  import ai.fal.client.*;
  import ai.fal.client.queue.*;

  var fal = FalClient.withEnvCredentials();

  var input = Map.of(
      "prompt", "a cat",
      "seed", 6252023,
      "image_size", "landscape_4_3",
      "num_images", 4
  );
  var result = fal.subscribe("fal-ai/flux/dev",
      SubscribeOptions.<JsonObject>builder()
          .input(input)
          .logs(true)
          .resultType(JsonObject.class)
          .onQueueUpdate(update -> {
              if (update instanceof QueueStatus.InProgress) {
                  System.out.println(((QueueStatus.InProgress) update).getLogs());
              }
          })
          .build()
  );
  ```
</CodeGroup>

## Supported Platforms

* Android (API 21+)
* JVM (Java 11+)
* Kotlin Multiplatform (JVM target)

## API Reference

<CardGroup cols={2}>
  <Card title="Java API Reference" icon="book" href="https://fal-ai.github.io/fal-java/fal-client/index.html">
    JavaDoc documentation
  </Card>

  <Card title="Kotlin API Reference" icon="book" href="https://fal-ai.github.io/fal-java/fal-client-kotlin/fal-client-kotlin/ai.fal.client.kt/index.html">
    KDoc documentation
  </Card>
</CardGroup>

<Card title="GitHub Repository" icon="github" href="https://github.com/fal-ai/fal-java">
  Source code and examples
</Card>
