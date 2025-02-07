### Software Design

Overall software design is concerned with the expandability, maintenance, reusability and testability.

Classes allow us to group related data and behaviour together. This makes it easier to read, understand and maintain the code. 
Furthermore, we can reuse code more efficiently, extend functionality without changing the original class due to
inheritance, and organise our code into more manageable units overall. One big file with only a few classes and extensive 
methods, however, will be challenging to navigate, modify as well as debug.

A complete lack of or even just sparse documentation in combination with an unstructured pile of code will, thus,  make it 
exceedingly difficult to gain an overview and manage the code in question. 

One of the fundamental software design principles which covers several issues with said unstructured pile of code is 
the SOLID Principle:
- Single responsibility - one class should only have one responsibility and only one reason to change
- Open/Closed - a class should be open for extension but closed for modification (existing code should not be changed)
- Liskov Substitution - a subclass should be able to replace its parent without changing the code
- Interface Segregation - a class should not have to implement irrelevant interfaces
- Dependency Inversion - high level moduls should not depend on low level moduls but rather abstractions

The KISS principle stands for 'Keep It Simple, Stupid' and literally means just that. Code should be as simple as possible
while still being effective, of course, and one should avoid unnecessary complexity and over-engineering wherever possible.

In conclusion, documentation, though often a pain in the a** to write, is essential for extensive projects. Especially
if they extend over longer periods of time and might not be handled by the same people from start to finish. Furthermore,
a clear structure with seperated clusters of related code will allow not only for a better reading and understanding but
also maintenance and debugging, thus making life easier for everyone involved.


## Design Patterns

Design patterns can help us solve common software design problems. They can be seen as an instruction manual which we can
adapt to solve recurring design problems in our code. A pattern, however, is not a particular code but rather a guideline
or concept which can be used to solve a certain problem. The implementation of such a pattern is, thus, individual to 
each problem.

### Decorator

### Template Method

The template methode is a behavioral design pattern which allows us to construct the basic framework of an algorithm in
the parent class, however, still allows the child class to change specific parts of the algorithm without changing its overall
structure. By breaking down the algorithm into smaller individual steps we can then use these to create methods
inside a template method. We can differentiate between two types of methods - abstract and optional. While abstract methods
must be implemented by all subclasses, optional steps can be overridden if needed. This distinction makes sense if
all of our child classes share a certain functionality but might still differ in other aspects, thus, require some liberties
regarding their execution.

For example, let's imagine we are tasked with writing a code for a dog-shelter database. It should keep track of the dogs'
health stats and provide us with information about possible treatments or needs overall. All of our subclasses will be based
on different breeds of dogs, as some needs are breed-specific. Our first step will be an analysis of the intended algorithm
so we can break it up into smaller steps and deliberate which ones our subclasses have in common and which ones will be 
different for all. For our example it will make sense to incorporate methods concerning all dogs alike in the parent class. 
These might be dietary and exercise requirements, methods keeping track of vet appointments and their medical history, 
age, sex or chip number. To ensure the implementation of these methods in all subclasses (breed classes), we will then create
an abstract parent class declaring the template method and incorporate the previously mentioned abstract methods. We can, 
however, further implement optional methods, which might not be relevant for all subclasses such as fur-type optionally 
providing information on whether or rather when they will need a bath and/or trim. The implementation of optional methods,
is not mandatory, as the name states, and they can also be overridden if needed.

In conclusion the template method allows us to reuse code without having to rewrite it and override certain parts of the
code without it having an effect on other parts of the algorithm. However, the scaffolding provided by this method may be
limiting and harder to maintain. 
