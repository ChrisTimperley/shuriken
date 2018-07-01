#ifndef H_FUNCTION_DB
#define H_FUNCTION_DB

#include <vector>
#include <string>

namespace bond {

class FunctionDB
{
public:
  FunctionDB();
  ~FunctionDB();

  class Entry {
  public:
    Entry(std::string const &name,
          std::string const &location,
          std::string const &return_type);

    std::string const name;
    std::string const location;
    std::string const return_type;
  }; // Entry

  void add(std::string const &name,
           std::string const &location,
           std::string const &return_type);
  void dump() const;

private:
  std::vector<Entry> contents;
}; // FunctionDB

} // bond

#endif // H_FUNCTION_DB
