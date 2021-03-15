import unittest

from unittest import mock

from GitHubAPI import git_hub_api

from typing import List,Any

class TestGitHubAPI(unittest.TestCase):
    @mock.patch('requests.get')
    def testgithubapi(self, mockedReq):
        """ Testing GitHubAPI"""
        mockedReq.return_value = MockResponse("['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5']")
        lis: List[Any] = git_hub_api("richkempinski")
        self.assertEqual(lis[0],'Repo: csp Number of commits: 2')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


# ['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5']