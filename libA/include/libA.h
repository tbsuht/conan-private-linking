#pragma once

#ifdef _WIN32
  #define libA_EXPORT __declspec(dllexport)
#else
  #define libA_EXPORT
#endif

libA_EXPORT void libA();
