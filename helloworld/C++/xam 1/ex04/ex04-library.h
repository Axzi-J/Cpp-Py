#ifndef EX04_LIBRARY_H_
#define EX04_LIBRARY_H_

class Buffer {
public:
    virtual void write(int v) = 0;
    virtual void clear() = 0;
    virtual ~Buffer();
};

// Task 4(a).  Declare the class CountingBuffer, by extending Buffer
// Write your code here

#endif /* EX04_LIBRARY_H_ */
