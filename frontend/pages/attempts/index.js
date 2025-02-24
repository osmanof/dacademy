import { AttemptsApi }                               from "@/lib/api";
import { formatDateTime, getTeacherServerSideProps } from "@/lib/utils";
import AppLayout                                     from "@/layouts/AppLayout";
import Table from "@/components/Table";
import ContentBlock from "@/components/ContentBlock";
import {Clear, Schedule} from "@mui/icons-material";

export async function getServerSideProps({req, res}) {
  try {
    const {props} = await getTeacherServerSideProps({req, res})

    const response = await AttemptsApi.list({queryParams: {statuses: '1,4'}, req, res})

    props.attempts = await response.json()

    return {props}
  } catch (e) {
    return e
  }
}

const statuses = {
  1: <Clear/>,
  4: <Schedule/>
}

export default function Page({profile, attempts}) {
  function generateAttemptsData(attempts) {
    let result = [];

    for (let i = 0; i < attempts.length; i ++) {
      let attempt = attempts[i];

      let task = attempt.task;
      let student = attempt.student;

      result.push(
          [i + 1,
            [task.title, `/attempts/${attempt.id}`],
            `${student.firstName} ${student.lastName}`,
            formatDateTime(attempt.createdAt),
            statuses[attempt.status]]);
    }

    return result;
  }

  return <AppLayout profile={profile}>
    <div className="container">

      <ContentBlock title="Задачи на проверку">
        { attempts.length ?
            <Table
                fields={
                  [
                    ["№", 6, "numberWithDot"],
                    ["Название задачи", 51, "link"],
                    ["Ученик", 17, "text"],
                    ["Дата", 16, "text"],
                    ["Статус", 10, "text"],
                  ]
                }

                data={generateAttemptsData(attempts)}
            /> : <p>Задач на проверку нет.</p>
        }
      </ContentBlock>

    </div>
  </AppLayout>
}
