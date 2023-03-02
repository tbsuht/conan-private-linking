#pragma once

#ifdef _WIN32
  #define libY_EXPORT __declspec(dllexport)
#else
  #define libY_EXPORT
#endif

libY_EXPORT void libY();
