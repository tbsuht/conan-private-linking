#pragma once

#ifdef _WIN32
  #define libB_EXPORT __declspec(dllexport)
#else
  #define libB_EXPORT
#endif

libB_EXPORT void libB();
