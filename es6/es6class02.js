function testable(target){
    target.isTestable = true;
}
@testable
class Example {}
Example.isTestable
