alfavit={
"и":
["*   **",
"*  * *",
"* *  *",
"**   *"],
"м":
["**    **",
"* *  * *",
"*  **  *",
"*      *",]}
a=input()
sa=a.split(' ')
for l in range(4):
    t=" "
    for i in sa:
        t+=alfavit[i][l]
    print(t)
