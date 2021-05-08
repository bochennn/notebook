## Operator Precedence ##

[运算符优先级顺序](https://en.cppreference.com/w/cpp/language/operator_precedence) [[chinese](https://blog.csdn.net/nicky_zs/article/details/4053146)]


| recedence | Operator | Description | Instance | Associativity |
| - | - | - | - | - |
| 1 | ()<br>[]<br>-><br>.<br>::<br>++<br>-- | 调节优先级的括号操作符<br>数组下标访问操作符<br>通过指向对象的指针访问成员的操作符<br>通过对象本身访问成员的操作符<br>作用域操作符<br>后置自增操作符<br>后置自减操作符 | (a + b) / 4;<br>array[4] = 2;<br>ptr->age = 34;<br>obj.age = 34;<br>Class::age = 2;<br>for( i = 0; i < 10; i++ ) ...<br>for( i = 10; i > 0; i-- ) ... | Left-to-right |
| 2 | !<br>~<br>++<br>--<br>-<br>+<br>*<br>&<br>(type)<br>sizeof | 逻辑取反操作符<br>按位取反(按位取补)<br>前置自增操作符<br>前置自减操作符<br>一元取负操作符<br>一元取正操作符<br>解引用操作符<br>取地址操作符<br>类型转换操作符<br>返回对象占用的字节数操作符 | if( !done ) ...<br>flags = ~flags;<br>for( i = 0; i < 10; ++i ) ...<br>for( i = 10; i > 0; --i ) ...<br>int i = -1;<br>int i = +1;<br>data = *ptr;<br>address = &obj;<br>int i = (int) floatNum;<br>int size = sizeof(floatNum); | Right-to-left |
| 3 | ->\*<br>.* | 在指针上通过指向成员的指针访问成员的操作符<br>在对象上通过指向成员的指针访问成员的操作符 | ptr->\*var = 24;<br>obj.*var = 24; | Left-to-right |
