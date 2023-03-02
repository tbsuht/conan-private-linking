#pragma once

#ifdef _WIN32
  #define libX_EXPORT __declspec(dllexport)
#else
  #define libX_EXPORT
#endif

libX_EXPORT void libX();
