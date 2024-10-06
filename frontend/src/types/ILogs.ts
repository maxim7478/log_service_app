export interface ILogsBackend {
  logs: string[],
  date_time: string,
}

export interface ILogsWsBackend extends ILogsBackend {
  id?: string,
}

export interface ILogData {
  logs: string[],
  lastUpdated: string,
}