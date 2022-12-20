## Overview

- Nest uses a 3 layer model consisting of the blow elements
	- `Controller` - access layer to your business logic. this handles the req/res process and is responsible for communication between server/client
	- `Module` - entrypoint into your application
	- `Service` - business logic

## Controllers 

> [!NOTE] HINT
> CRUD controllers w/ validation can be created through `nest g resource [name]`

purpose is to receive **specific** requests for the application. each controller can have more than one route. 

controllers are created using *classes* and *decorators* 
	- decorators associate the classes with their metadata + enables Nest to create a routing map  (determine which req goes to the controller)
	- `@Controller(<prefix>)` decorator is **required** to create a controller and it'll create a controller prefixed by `<prefix>` . 
	- can use the `@<HTTP verb>(<sub-prefix>)` method to set it as a get/post etc with the path `<prefix>/<subprefix>`
	- we can access the request object using the `@Req()` decorator
	- route parameters can be accessed through the `@Param()` decorator and declaration of that route in the http verb decorator 
	- similarly, `@Body()` can be used to access the request body
	- refer [here](https://docs.nestjs.com/controllers) for a list of decorators and a more indepth write-up of controllers in nest

> [!NOTE] HINT
> create a controller thorugh cli using `nest g controller [prefix]`

### Request payloads

Nest requires us to define DTOs in order to define and validate the shape of the data that is transported over the wire. 
	- nest prefers using **classes** over interfaces because classes carry actual runtime values (as classes are actual JS constructs)

### Linking 

NestJS requires us to link the controller to a module for Nest to know that the controller exists. This is done through the `controllers` property like so: 

```typescript
import { Module } from '@nestjs/common';
import { CatsController } from './cats/cats.controller';

@Module({
  controllers: [CatsController],
})
export class AppModule {}
```

### Library specific approach

Rather than using the nestJS exposed decorators, we can instead use the general `@Res()` decorator and type the type of the response object ourselves. 

Doing so makes the code platform dependent as underlying libs may have different APIs on the response object


## Providers 

Providers can be injected as a dependency and nest will figure out the wiring at runtime. In other words, providers *provide* some capability to the wrapper. 

We need to declare the provider with the `@Injectable()` decorator to tell the NestJS runtime that this is a dependency that is managed by the NestJS IoC container

> [!NOTE] Hint
> We can use `nest g service <name>` to create a service using the cli 

when injecting, we can simply put this in the constructor of the class that requires this and set visibility to `private` to skip initialisation

```typescript
@Controller('cats')
export class CatsController {
  constructor(private catsService: CatsService) {}
}
```

### Property based injection

can also insert a property rathber than through the constructor method. This can be done through calling the `@Inject(<name>)` decorator. 

**however,** if the class doesn't `extend` another class, doing injection using the constructor is ideal.

### Provider registration

once we have a provider/consumer, we need to hand over the deps management to nest. this can be done through: 

```typescript
@Module({
  controllers: [<list of controllers>], 
  prpvoders: [<list of providers>]
})

export class AppModule {}
```

## Modules 

a module is a class annotated w/ the `@Module()` decorator; this provides metadata that nest uses to organise the app structure
	-configuration object has 4 properties: `providers/controllers/imports/exports`

> [!NOTE] HINT
> we can initialise this using the cli through `nest g module <name>`

**modules are singletons by default** 
- this allows modules to be reshared easily and modules can also re-export their shared services
- modules can also **inject providers**

#### Scoping

Nest encapsulates proividers inside the module scope
	- this means that by default, **you cannot use a module's providers anywhere else wihtout first importing the module**. 
	- however, some providers might be reshared widely and in order to ease access to the provider (and the module by extension), we can use the `@Global()` decorator for the module (however, this is **not recommended**)

#### Dynamic modules

dynamic modules are modules that *can be customised by the caller*. this is done through exposing a method `forRoot` on the module root. 
	- the properties on the dynamic module **extend** rather than override the default `@Module(...)` decorator properties.