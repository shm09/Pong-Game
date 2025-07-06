#include <iostream>
#include "raylib.h"
int main() {
    std::cout << "Hello, world! From Linux 124" << std::endl;

    InitWindow(800, 600, "Hello World");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawText("Hello, world! From Linux 124", 190, 200, 20, LIGHTGRAY);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}